# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T15:37:31.792531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1691` n `12`; crypto_alt avg `0.1365` n `233`; crypto_major avg `0.074` n `8`; equity avg `0.4269` n `136`; fx avg `-0.0237` n `6`; index avg `0.11` n `27`; metal avg `0.1488` n `20`; unknown avg `0.4111` n `894`
- 1h: commodity avg `-0.2217` n `12`; crypto_alt avg `0.1393` n `233`; crypto_major avg `0.1113` n `8`; equity avg `0.6655` n `136`; fx avg `-0.0312` n `6`; index avg `0.1226` n `27`; metal avg `0.2148` n `20`; unknown avg `0.1067` n `878`
- 4h: commodity avg `-0.1566` n `12`; crypto_alt avg `-0.1872` n `233`; crypto_major avg `0.038` n `8`; equity avg `0.6506` n `136`; fx avg `-0.0275` n `6`; index avg `0.037` n `27`; metal avg `0.1115` n `20`; unknown avg `0.5536` n `872`
- 24h: commodity avg `0.3774` n `12`; crypto_alt avg `-0.1829` n `233`; crypto_major avg `1.4509` n `8`; equity avg `-0.2522` n `136`; fx avg `0.0211` n `6`; index avg `-0.1767` n `27`; metal avg `-0.337` n `20`; unknown avg `0.9565` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
