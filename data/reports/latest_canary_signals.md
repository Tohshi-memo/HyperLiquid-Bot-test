# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T10:22:29.745011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0646` n `13`; crypto_alt avg `0.0532` n `238`; crypto_major avg `0.0589` n `8`; equity avg `0.0704` n `156`; fx avg `-0.0091` n `6`; index avg `0.0048` n `27`; metal avg `0.0013` n `20`; unknown avg `1.8882` n `1264`
- 1h: commodity avg `0.1078` n `13`; crypto_alt avg `-0.3244` n `238`; crypto_major avg `-0.3585` n `8`; equity avg `0.0106` n `156`; fx avg `-0.0234` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0341` n `20`; unknown avg `2.0741` n `1258`
- 4h: commodity avg `-0.141` n `13`; crypto_alt avg `-0.6075` n `238`; crypto_major avg `-0.4221` n `8`; equity avg `0.0396` n `156`; fx avg `0.0787` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0973` n `20`; unknown avg `9.3753` n `1168`
- 24h: commodity avg `-0.4803` n `13`; crypto_alt avg `-2.4211` n `238`; crypto_major avg `-0.8132` n `8`; equity avg `0.9381` n `156`; fx avg `0.2842` n `6`; index avg `0.2999` n `27`; metal avg `0.0405` n `20`; unknown avg `4.8255` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1868`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
