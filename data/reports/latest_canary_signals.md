# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T10:52:27.941766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0555` n `13`; crypto_alt avg `0.1114` n `238`; crypto_major avg `0.0789` n `8`; equity avg `0.007` n `156`; fx avg `-0.014` n `6`; index avg `0.005` n `27`; metal avg `0.0075` n `20`; unknown avg `-0.0464` n `1264`
- 1h: commodity avg `0.0335` n `13`; crypto_alt avg `-0.0789` n `238`; crypto_major avg `-0.1277` n `8`; equity avg `-0.1718` n `156`; fx avg `-0.0288` n `6`; index avg `-0.0116` n `27`; metal avg `0.0175` n `20`; unknown avg `1.4249` n `1258`
- 4h: commodity avg `-0.1638` n `13`; crypto_alt avg `-0.3292` n `238`; crypto_major avg `-0.1725` n `8`; equity avg `-0.0655` n `156`; fx avg `0.0167` n `6`; index avg `-0.018` n `27`; metal avg `-0.0712` n `20`; unknown avg `7.2003` n `1170`
- 24h: commodity avg `-0.5219` n `13`; crypto_alt avg `-2.2022` n `238`; crypto_major avg `-0.6675` n `8`; equity avg `0.8365` n `156`; fx avg `0.2542` n `6`; index avg `0.2852` n `27`; metal avg `0.0461` n `20`; unknown avg `25.882` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
