# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T06:52:33.257632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `0.0381` n `234`; crypto_major avg `0.1326` n `8`; equity avg `-0.0381` n `141`; fx avg `0.0053` n `6`; index avg `-0.008` n `26`; metal avg `-0.0001` n `20`; unknown avg `2.0886` n `946`
- 1h: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.1307` n `234`; crypto_major avg `-0.0801` n `8`; equity avg `0.0981` n `141`; fx avg `-0.0067` n `6`; index avg `0.0175` n `26`; metal avg `0.0364` n `20`; unknown avg `1.6212` n `912`
- 4h: commodity avg `-0.0515` n `12`; crypto_alt avg `0.3586` n `234`; crypto_major avg `-0.0306` n `8`; equity avg `0.4607` n `141`; fx avg `-0.0423` n `6`; index avg `0.0865` n `26`; metal avg `0.0111` n `20`; unknown avg `2.5942` n `906`
- 24h: commodity avg `0.1975` n `12`; crypto_alt avg `1.6459` n `234`; crypto_major avg `0.4066` n `8`; equity avg `1.1382` n `141`; fx avg `-0.1707` n `6`; index avg `0.1792` n `26`; metal avg `-0.0583` n `20`; unknown avg `13.1163` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
