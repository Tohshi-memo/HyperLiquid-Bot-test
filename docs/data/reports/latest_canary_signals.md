# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T12:37:29.281659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0387` n `13`; crypto_alt avg `-0.3548` n `238`; crypto_major avg `-0.2591` n `8`; equity avg `-0.3861` n `156`; fx avg `0.0016` n `6`; index avg `-0.0218` n `27`; metal avg `-0.0778` n `20`; unknown avg `38.1252` n `1265`
- 1h: commodity avg `0.101` n `13`; crypto_alt avg `0.0246` n `238`; crypto_major avg `-0.0204` n `8`; equity avg `-0.319` n `156`; fx avg `0.0129` n `6`; index avg `-0.0237` n `27`; metal avg `-0.0835` n `20`; unknown avg `0.5504` n `1252`
- 4h: commodity avg `0.1085` n `13`; crypto_alt avg `-0.3267` n `238`; crypto_major avg `-0.3914` n `8`; equity avg `-0.3452` n `156`; fx avg `0.0315` n `6`; index avg `-0.0063` n `27`; metal avg `-0.1149` n `20`; unknown avg `3.1318` n `1250`
- 24h: commodity avg `-0.4699` n `13`; crypto_alt avg `-1.9373` n `238`; crypto_major avg `-0.4545` n `8`; equity avg `0.533` n `156`; fx avg `0.2868` n `6`; index avg `0.27` n `27`; metal avg `-0.0375` n `20`; unknown avg `3.8925` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
