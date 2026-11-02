# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T11:52:36.687324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.034` n `13`; crypto_alt avg `-0.0146` n `238`; crypto_major avg `-0.0666` n `8`; equity avg `-0.0339` n `156`; fx avg `0.0029` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0244` n `20`; unknown avg `18.7657` n `1264`
- 1h: commodity avg `-0.0719` n `13`; crypto_alt avg `-0.0264` n `238`; crypto_major avg `-0.1303` n `8`; equity avg `-0.0546` n `156`; fx avg `0.0197` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0291` n `20`; unknown avg `0.349` n `1258`
- 4h: commodity avg `-0.181` n `13`; crypto_alt avg `-0.2898` n `238`; crypto_major avg `-0.0768` n `8`; equity avg `0.0016` n `156`; fx avg `0.0187` n `6`; index avg `0.0006` n `27`; metal avg `-0.0936` n `20`; unknown avg `7.3591` n `1194`
- 24h: commodity avg `-0.5803` n `13`; crypto_alt avg `-2.0794` n `238`; crypto_major avg `-0.7032` n `8`; equity avg `0.7448` n `156`; fx avg `0.2849` n `6`; index avg `0.2874` n `27`; metal avg `0.0046` n `20`; unknown avg `3.8816` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
