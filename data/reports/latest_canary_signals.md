# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T11:22:26.529416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0399` n `13`; crypto_alt avg `0.3235` n `235`; crypto_major avg `0.1447` n `8`; equity avg `0.0492` n `151`; fx avg `-0.0024` n `6`; index avg `0.0117` n `26`; metal avg `0.0435` n `20`; unknown avg `0.0925` n `1136`
- 1h: commodity avg `-0.0406` n `13`; crypto_alt avg `0.2588` n `235`; crypto_major avg `0.2609` n `8`; equity avg `-0.2315` n `151`; fx avg `0.0057` n `6`; index avg `-0.0264` n `26`; metal avg `-0.0189` n `20`; unknown avg `0.264` n `1133`
- 4h: commodity avg `0.0081` n `13`; crypto_alt avg `-0.4879` n `235`; crypto_major avg `-0.0793` n `8`; equity avg `-0.2999` n `151`; fx avg `0.0164` n `6`; index avg `-0.0062` n `26`; metal avg `0.016` n `20`; unknown avg `1193.0229` n `1037`
- 24h: commodity avg `1.0625` n `13`; crypto_alt avg `0.0485` n `235`; crypto_major avg `0.1103` n `8`; equity avg `-0.2099` n `151`; fx avg `0.0227` n `6`; index avg `0.022` n `26`; metal avg `-0.4539` n `20`; unknown avg `1268.4267` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1514`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1302`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0756`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
