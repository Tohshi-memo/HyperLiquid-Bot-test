# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T21:37:32.869112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.0584` n `230`; crypto_major avg `-0.0582` n `8`; equity avg `0.0326` n `92`; fx avg `0.0012` n `6`; index avg `0.0042` n `25`; metal avg `0.0151` n `20`; unknown avg `0.0349` n `768`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `0.195` n `230`; crypto_major avg `0.2208` n `8`; equity avg `0.045` n `92`; fx avg `-0.0027` n `6`; index avg `0.0123` n `25`; metal avg `0.0359` n `20`; unknown avg `-0.4918` n `768`
- 4h: commodity avg `0.1717` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `0.4366` n `8`; equity avg `0.2342` n `92`; fx avg `-0.0` n `6`; index avg `-0.0096` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.1916` n `767`
- 24h: commodity avg `0.3166` n `12`; crypto_alt avg `2.7362` n `230`; crypto_major avg `4.161` n `8`; equity avg `1.4849` n `92`; fx avg `-0.0197` n `6`; index avg `0.4235` n `25`; metal avg `0.6055` n `20`; unknown avg `0.2997` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
