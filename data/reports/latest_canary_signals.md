# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T15:52:39.362840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.3417` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8658` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0228` n `13`; crypto_alt avg `0.2047` n `239`; crypto_major avg `0.1639` n `8`; equity avg `0.4525` n `160`; fx avg `-0.0028` n `6`; index avg `0.0334` n `27`; metal avg `-0.0235` n `20`; unknown avg `-0.0716` n `1261`
- 1h: commodity avg `0.1195` n `13`; crypto_alt avg `0.6783` n `239`; crypto_major avg `0.4787` n `8`; equity avg `1.3093` n `160`; fx avg `-0.0027` n `6`; index avg `0.1062` n `27`; metal avg `-0.0154` n `20`; unknown avg `0.6696` n `1255`
- 4h: commodity avg `0.3684` n `13`; crypto_alt avg `2.3853` n `239`; crypto_major avg `1.964` n `8`; equity avg `4.3057` n `160`; fx avg `0.0097` n `6`; index avg `0.4198` n `27`; metal avg `0.0982` n `20`; unknown avg `24.1948` n `1249`
- 24h: commodity avg `-0.2456` n `13`; crypto_alt avg `1.0607` n `239`; crypto_major avg `-1.8301` n `8`; equity avg `4.0368` n `160`; fx avg `-0.1379` n `6`; index avg `0.4347` n `27`; metal avg `0.4759` n `20`; unknown avg `6.8155` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
