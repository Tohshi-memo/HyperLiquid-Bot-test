# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T13:22:26.751630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `13`; crypto_alt avg `0.0866` n `239`; crypto_major avg `0.0132` n `8`; equity avg `0.0646` n `160`; fx avg `-0.0048` n `6`; index avg `0.0127` n `27`; metal avg `-0.0269` n `20`; unknown avg `18.7128` n `1262`
- 1h: commodity avg `-0.165` n `13`; crypto_alt avg `-0.0214` n `239`; crypto_major avg `-0.0518` n `8`; equity avg `-0.3113` n `160`; fx avg `-0.0155` n `6`; index avg `-0.0109` n `27`; metal avg `-0.0345` n `20`; unknown avg `19.1465` n `1256`
- 4h: commodity avg `-0.0725` n `13`; crypto_alt avg `-0.2343` n `239`; crypto_major avg `-0.4007` n `8`; equity avg `-0.8899` n `160`; fx avg `-0.0249` n `6`; index avg `-0.0423` n `27`; metal avg `-0.1335` n `20`; unknown avg `319.1378` n `1250`
- 24h: commodity avg `-0.584` n `13`; crypto_alt avg `-0.3138` n `239`; crypto_major avg `-0.5847` n `8`; equity avg `2.8626` n `160`; fx avg `-0.0411` n `6`; index avg `0.3724` n `27`; metal avg `-0.1532` n `20`; unknown avg `2.9015` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2266`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
