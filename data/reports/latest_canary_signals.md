# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T19:22:33.209426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2382` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0717` n `13`; crypto_alt avg `0.0369` n `238`; crypto_major avg `0.0001` n `8`; equity avg `0.2591` n `156`; fx avg `0.0073` n `6`; index avg `0.011` n `27`; metal avg `0.0104` n `20`; unknown avg `9.0053` n `1261`
- 1h: commodity avg `-0.0857` n `13`; crypto_alt avg `-0.1016` n `238`; crypto_major avg `-0.14` n `8`; equity avg `0.5523` n `156`; fx avg `0.0097` n `6`; index avg `0.0383` n `27`; metal avg `0.0383` n `20`; unknown avg `7.4968` n `1255`
- 4h: commodity avg `-0.0566` n `13`; crypto_alt avg `-1.3438` n `238`; crypto_major avg `-1.402` n `8`; equity avg `-1.2551` n `156`; fx avg `0.0499` n `6`; index avg `-0.1638` n `27`; metal avg `-0.1939` n `20`; unknown avg `8.5932` n `1251`
- 24h: commodity avg `0.3609` n `13`; crypto_alt avg `-4.6378` n `238`; crypto_major avg `-4.3922` n `8`; equity avg `-5.7571` n `156`; fx avg `-0.0727` n `6`; index avg `-0.5453` n `27`; metal avg `-1.0273` n `20`; unknown avg `46.5941` n `1038`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1928`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
