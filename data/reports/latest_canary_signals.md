# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T11:07:32.355725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `13`; crypto_alt avg `0.0057` n `238`; crypto_major avg `-0.0732` n `8`; equity avg `0.0558` n `156`; fx avg `0.0062` n `6`; index avg `0.0067` n `27`; metal avg `0.0161` n `20`; unknown avg `-0.0066` n `1258`
- 1h: commodity avg `-0.0205` n `13`; crypto_alt avg `0.1387` n `238`; crypto_major avg `0.0396` n `8`; equity avg `-0.0244` n `156`; fx avg `-0.0279` n `6`; index avg `0.0029` n `27`; metal avg `0.0367` n `20`; unknown avg `1.8057` n `1258`
- 4h: commodity avg `-0.1654` n `13`; crypto_alt avg `-0.4115` n `238`; crypto_major avg `-0.1733` n `8`; equity avg `-0.0549` n `156`; fx avg `0.0331` n `6`; index avg `-0.006` n `27`; metal avg `-0.0513` n `20`; unknown avg `7.4959` n `1170`
- 24h: commodity avg `-0.5281` n `13`; crypto_alt avg `-2.1674` n `238`; crypto_major avg `-0.658` n `8`; equity avg `0.9006` n `156`; fx avg `0.2654` n `6`; index avg `0.2942` n `27`; metal avg `0.0625` n `20`; unknown avg `3.7812` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
