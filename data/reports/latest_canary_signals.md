# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T20:37:25.384586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3152` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2354` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0257` n `13`; crypto_alt avg `-0.3319` n `239`; crypto_major avg `-0.3129` n `8`; equity avg `-0.7852` n `168`; fx avg `-0.0039` n `6`; index avg `-0.0787` n `27`; metal avg `-0.0897` n `20`; unknown avg `11.3212` n `1267`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `-0.5065` n `239`; crypto_major avg `-0.4839` n `8`; equity avg `-1.057` n `168`; fx avg `-0.003` n `6`; index avg `-0.1091` n `27`; metal avg `0.0509` n `20`; unknown avg `217.7546` n `1255`
- 4h: commodity avg `0.1094` n `13`; crypto_alt avg `3.4977` n `239`; crypto_major avg `3.4246` n `8`; equity avg `4.7124` n `168`; fx avg `0.0699` n `6`; index avg `0.4677` n `27`; metal avg `1.1892` n `20`; unknown avg `18.1814` n `1254`
- 24h: commodity avg `0.3855` n `13`; crypto_alt avg `2.3978` n `239`; crypto_major avg `1.4507` n `8`; equity avg `-0.8993` n `168`; fx avg `0.0474` n `6`; index avg `-0.1042` n `27`; metal avg `0.147` n `20`; unknown avg `23.2428` n `1087`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
