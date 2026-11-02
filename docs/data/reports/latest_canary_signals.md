# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T02:07:29.857141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0684` n `13`; crypto_alt avg `-0.053` n `238`; crypto_major avg `-0.1059` n `8`; equity avg `-0.0079` n `156`; fx avg `0.0172` n `6`; index avg `0.0084` n `27`; metal avg `0.0421` n `20`; unknown avg `1.0297` n `1255`
- 1h: commodity avg `-0.1267` n `13`; crypto_alt avg `0.0493` n `238`; crypto_major avg `0.2183` n `8`; equity avg `-0.1096` n `156`; fx avg `0.011` n `6`; index avg `0.0082` n `27`; metal avg `-0.0624` n `20`; unknown avg `1.1307` n `1251`
- 4h: commodity avg `-0.1576` n `13`; crypto_alt avg `0.132` n `238`; crypto_major avg `0.651` n `8`; equity avg `0.5191` n `156`; fx avg `0.1316` n `6`; index avg `0.2175` n `27`; metal avg `0.1139` n `20`; unknown avg `0.9229` n `1221`
- 24h: commodity avg `-0.2118` n `13`; crypto_alt avg `-0.4923` n `238`; crypto_major avg `0.2815` n `8`; equity avg `0.7742` n `156`; fx avg `0.1211` n `6`; index avg `0.2686` n `27`; metal avg `0.1382` n `20`; unknown avg `1.9869` n `1120`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
