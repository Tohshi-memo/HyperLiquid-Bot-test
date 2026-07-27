# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T08:52:27.324982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.0802` n `230`; crypto_major avg `-0.0919` n `8`; equity avg `-0.0356` n `100`; fx avg `-0.0032` n `6`; index avg `-0.0037` n `25`; metal avg `-0.0278` n `20`; unknown avg `-0.0474` n `775`
- 1h: commodity avg `-0.1935` n `12`; crypto_alt avg `-0.2896` n `230`; crypto_major avg `-0.1576` n `8`; equity avg `0.0431` n `100`; fx avg `0.0087` n `6`; index avg `0.0309` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0849` n `775`
- 4h: commodity avg `-0.4312` n `12`; crypto_alt avg `-0.3482` n `230`; crypto_major avg `-0.0262` n `8`; equity avg `0.4965` n `100`; fx avg `0.0089` n `6`; index avg `0.0946` n `25`; metal avg `0.1401` n `20`; unknown avg `-0.0611` n `759`
- 24h: commodity avg `-0.9053` n `12`; crypto_alt avg `0.4862` n `230`; crypto_major avg `1.2122` n `8`; equity avg `1.4366` n `100`; fx avg `0.1267` n `6`; index avg `0.2004` n `25`; metal avg `0.4279` n `20`; unknown avg `-0.0324` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
