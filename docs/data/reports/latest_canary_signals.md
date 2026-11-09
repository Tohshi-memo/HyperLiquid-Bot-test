# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T18:37:31.905056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.2955` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0233` n `13`; crypto_alt avg `-0.1553` n `239`; crypto_major avg `-0.1801` n `8`; equity avg `0.0033` n `160`; fx avg `0.0021` n `6`; index avg `0.0082` n `27`; metal avg `0.032` n `20`; unknown avg `0.1181` n `1259`
- 1h: commodity avg `0.1025` n `13`; crypto_alt avg `0.1305` n `239`; crypto_major avg `-0.0175` n `8`; equity avg `-0.1877` n `160`; fx avg `0.0008` n `6`; index avg `-0.0148` n `27`; metal avg `0.0372` n `20`; unknown avg `0.0164` n `1255`
- 4h: commodity avg `0.1369` n `13`; crypto_alt avg `0.0954` n `239`; crypto_major avg `0.1125` n `8`; equity avg `2.408` n `160`; fx avg `-0.0102` n `6`; index avg `0.2564` n `27`; metal avg `0.0211` n `20`; unknown avg `1.3633` n `1249`
- 24h: commodity avg `-0.0201` n `13`; crypto_alt avg `0.1506` n `239`; crypto_major avg `-2.8339` n `8`; equity avg `3.3502` n `160`; fx avg `-0.139` n `6`; index avg `0.428` n `27`; metal avg `0.4051` n `20`; unknown avg `3.9538` n `1074`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1758`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1509`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1452`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1313`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.119`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.108`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1018`, n `669`, weak_sample_signal
