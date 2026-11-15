# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T12:22:31.041927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3824` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2244` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9683` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `0.2959` n `239`; crypto_major avg `0.3654` n `8`; equity avg `0.0092` n `162`; fx avg `0.0054` n `6`; index avg `-0.0011` n `27`; metal avg `0.0226` n `20`; unknown avg `0.1407` n `1259`
- 1h: commodity avg `0.0122` n `13`; crypto_alt avg `0.2912` n `239`; crypto_major avg `0.1617` n `8`; equity avg `-0.0582` n `162`; fx avg `-0.0047` n `6`; index avg `-0.0073` n `27`; metal avg `0.0247` n `20`; unknown avg `159.3117` n `1253`
- 4h: commodity avg `-0.0265` n `13`; crypto_alt avg `1.9718` n `239`; crypto_major avg `2.3559` n `8`; equity avg `0.3876` n `162`; fx avg `-0.0229` n `6`; index avg `0.0406` n `27`; metal avg `0.1315` n `20`; unknown avg `0.2606` n `1253`
- 24h: commodity avg `0.0332` n `13`; crypto_alt avg `-3.4865` n `239`; crypto_major avg `-2.7076` n `8`; equity avg `-0.6974` n `162`; fx avg `0.0014` n `6`; index avg `-0.0586` n `27`; metal avg `-0.3106` n `20`; unknown avg `-0.2226` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
