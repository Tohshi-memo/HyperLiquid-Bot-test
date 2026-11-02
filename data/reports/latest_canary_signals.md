# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T00:22:29.477082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.528` n `238`; crypto_major avg `-0.4565` n `8`; equity avg `-0.1273` n `156`; fx avg `0.0256` n `6`; index avg `0.0185` n `27`; metal avg `-0.038` n `20`; unknown avg `2.335` n `1261`
- 1h: commodity avg `0.0744` n `13`; crypto_alt avg `-0.4458` n `238`; crypto_major avg `-0.1492` n `8`; equity avg `0.1078` n `156`; fx avg `0.0412` n `6`; index avg `0.0868` n `27`; metal avg `0.0323` n `20`; unknown avg `-0.0442` n `1249`
- 4h: commodity avg `0.0636` n `13`; crypto_alt avg `-0.0048` n `238`; crypto_major avg `0.2509` n `8`; equity avg `0.2657` n `156`; fx avg `0.0577` n `6`; index avg `0.0942` n `27`; metal avg `0.1251` n `20`; unknown avg `21.2013` n `1219`
- 24h: commodity avg `-0.0041` n `13`; crypto_alt avg `-0.7742` n `238`; crypto_major avg `-0.1424` n `8`; equity avg `0.4746` n `156`; fx avg `0.0574` n `6`; index avg `0.1309` n `27`; metal avg `0.1436` n `20`; unknown avg `3.7721` n `1114`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
