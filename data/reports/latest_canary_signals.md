# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T07:22:34.586972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `13`; crypto_alt avg `-0.0954` n `239`; crypto_major avg `-0.2208` n `8`; equity avg `0.0678` n `164`; fx avg `0.0178` n `6`; index avg `0.0083` n `27`; metal avg `-0.0299` n `20`; unknown avg `2.3317` n `1264`
- 1h: commodity avg `0.0095` n `13`; crypto_alt avg `0.1813` n `239`; crypto_major avg `0.1531` n `8`; equity avg `0.6856` n `164`; fx avg `0.0397` n `6`; index avg `0.0858` n `27`; metal avg `0.0254` n `20`; unknown avg `246.7368` n `1258`
- 4h: commodity avg `0.089` n `13`; crypto_alt avg `0.9263` n `239`; crypto_major avg `1.6703` n `8`; equity avg `1.7383` n `164`; fx avg `0.04` n `6`; index avg `0.2604` n `27`; metal avg `0.3405` n `20`; unknown avg `2.9189` n `1207`
- 24h: commodity avg `0.3569` n `13`; crypto_alt avg `-0.0422` n `239`; crypto_major avg `-0.7559` n `8`; equity avg `0.3222` n `164`; fx avg `-0.0531` n `6`; index avg `0.1884` n `27`; metal avg `-0.277` n `20`; unknown avg `93.7027` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
