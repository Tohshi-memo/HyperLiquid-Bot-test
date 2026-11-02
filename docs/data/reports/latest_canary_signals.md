# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T05:52:26.196085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0555` n `13`; crypto_alt avg `-0.0594` n `238`; crypto_major avg `0.0238` n `8`; equity avg `0.046` n `156`; fx avg `-0.0053` n `6`; index avg `-0.0042` n `27`; metal avg `0.03` n `20`; unknown avg `0.6264` n `1264`
- 1h: commodity avg `-0.0314` n `13`; crypto_alt avg `-0.1899` n `238`; crypto_major avg `-0.0211` n `8`; equity avg `0.0031` n `156`; fx avg `-0.0242` n `6`; index avg `0.0249` n `27`; metal avg `0.1986` n `20`; unknown avg `0.0263` n `1251`
- 4h: commodity avg `-0.2807` n `13`; crypto_alt avg `-0.284` n `238`; crypto_major avg `-0.0785` n `8`; equity avg `0.7655` n `156`; fx avg `0.0715` n `6`; index avg `0.1455` n `27`; metal avg `0.1474` n `20`; unknown avg `2.3653` n `1193`
- 24h: commodity avg `-0.4146` n `13`; crypto_alt avg `-1.0418` n `238`; crypto_major avg `0.2839` n `8`; equity avg `1.3563` n `156`; fx avg `0.1798` n `6`; index avg `0.3776` n `27`; metal avg `0.2452` n `20`; unknown avg `3.3343` n `1070`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
