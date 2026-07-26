# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T21:52:27.496998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.074` n `12`; crypto_alt avg `0.0652` n `230`; crypto_major avg `0.0955` n `8`; equity avg `0.02` n `100`; fx avg `-0.0013` n `6`; index avg `-0.0034` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0377` n `775`
- 1h: commodity avg `-0.1277` n `12`; crypto_alt avg `0.3447` n `230`; crypto_major avg `0.3368` n `8`; equity avg `0.094` n `100`; fx avg `-0.007` n `6`; index avg `0.0001` n `25`; metal avg `0.0613` n `20`; unknown avg `-0.0178` n `775`
- 4h: commodity avg `0.0715` n `12`; crypto_alt avg `0.1002` n `230`; crypto_major avg `0.1983` n `8`; equity avg `0.06` n `100`; fx avg `0.0346` n `6`; index avg `-0.0483` n `25`; metal avg `0.0808` n `20`; unknown avg `-0.3488` n `775`
- 24h: commodity avg `-0.3749` n `12`; crypto_alt avg `0.9249` n `230`; crypto_major avg `1.109` n `8`; equity avg `0.7159` n `100`; fx avg `0.0445` n `6`; index avg `0.0947` n `25`; metal avg `0.2544` n `20`; unknown avg `-0.0239` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
