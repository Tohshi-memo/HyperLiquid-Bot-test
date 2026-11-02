# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T10:37:42.706044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `-0.0327` n `238`; crypto_major avg `-0.0249` n `8`; equity avg `-0.1571` n `156`; fx avg `-0.011` n `6`; index avg `-0.0136` n `27`; metal avg `0.0118` n `20`; unknown avg `1.5407` n `1264`
- 1h: commodity avg `0.0776` n `13`; crypto_alt avg `-0.1257` n `238`; crypto_major avg `-0.155` n `8`; equity avg `-0.0821` n `156`; fx avg `-0.0179` n `6`; index avg `-0.0216` n `27`; metal avg `-0.021` n `20`; unknown avg `1.3171` n `1258`
- 4h: commodity avg `-0.1364` n `13`; crypto_alt avg `-0.4577` n `238`; crypto_major avg `-0.294` n `8`; equity avg `-0.0691` n `156`; fx avg `0.0461` n `6`; index avg `-0.0204` n `27`; metal avg `-0.06` n `20`; unknown avg `10.3086` n `1170`
- 24h: commodity avg `-0.4695` n `13`; crypto_alt avg `-2.2811` n `238`; crypto_major avg `-0.7422` n `8`; equity avg `0.7774` n `156`; fx avg `0.2695` n `6`; index avg `0.288` n `27`; metal avg `0.0312` n `20`; unknown avg `3.9398` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
