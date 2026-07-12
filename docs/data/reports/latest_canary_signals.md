# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T23:37:26.163372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0583` n `230`; crypto_major avg `-0.0112` n `8`; equity avg `-0.0211` n `92`; fx avg `0.0034` n `6`; index avg `0.0059` n `25`; metal avg `0.0119` n `20`; unknown avg `-0.0306` n `766`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0002` n `230`; crypto_major avg `0.0738` n `8`; equity avg `-0.0827` n `92`; fx avg `0.008` n `6`; index avg `0.0023` n `25`; metal avg `-0.024` n `20`; unknown avg `-0.0337` n `765`
- 4h: commodity avg `-0.1307` n `12`; crypto_alt avg `-0.9745` n `230`; crypto_major avg `-0.8446` n `8`; equity avg `-0.4409` n `92`; fx avg `-0.0463` n `6`; index avg `-0.0932` n `25`; metal avg `-0.2503` n `20`; unknown avg `0.1351` n `765`
- 24h: commodity avg `0.0875` n `12`; crypto_alt avg `-0.7655` n `230`; crypto_major avg `-0.2312` n `8`; equity avg `-0.373` n `92`; fx avg `-0.0685` n `6`; index avg `-0.0756` n `25`; metal avg `-0.332` n `20`; unknown avg `0.3087` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
