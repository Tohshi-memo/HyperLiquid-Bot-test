# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T19:37:29.582430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0305` n `13`; crypto_alt avg `-0.2365` n `237`; crypto_major avg `-0.1587` n `8`; equity avg `-0.1337` n `154`; fx avg `0.0046` n `6`; index avg `-0.0187` n `27`; metal avg `-0.0085` n `20`; unknown avg `133.7644` n `1238`
- 1h: commodity avg `0.1012` n `13`; crypto_alt avg `-0.1187` n `237`; crypto_major avg `-0.2149` n `8`; equity avg `-0.1454` n `154`; fx avg `-0.0028` n `6`; index avg `-0.0188` n `27`; metal avg `-0.0382` n `20`; unknown avg `13.9982` n `1236`
- 4h: commodity avg `-0.0267` n `13`; crypto_alt avg `-1.2399` n `237`; crypto_major avg `-0.6748` n `8`; equity avg `-0.3724` n `154`; fx avg `-0.0251` n `6`; index avg `-0.0595` n `27`; metal avg `-0.1347` n `20`; unknown avg `7.7771` n `1230`
- 24h: commodity avg `-0.1332` n `13`; crypto_alt avg `-0.6206` n `237`; crypto_major avg `-0.1559` n `8`; equity avg `0.5933` n `153`; fx avg `0.0274` n `6`; index avg `-0.0971` n `27`; metal avg `0.0196` n `20`; unknown avg `782.3207` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
