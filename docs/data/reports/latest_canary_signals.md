# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T12:01:33.114766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `-0.0349` n `230`; crypto_major avg `-0.0545` n `8`; equity avg `-0.0392` n `98`; fx avg `0.0008` n `6`; index avg `-0.0076` n `25`; metal avg `0.0364` n `20`; unknown avg `0.0368` n `773`
- 1h: commodity avg `0.1085` n `12`; crypto_alt avg `-0.1563` n `230`; crypto_major avg `-0.2066` n `8`; equity avg `-0.4481` n `98`; fx avg `0.002` n `6`; index avg `-0.0728` n `25`; metal avg `0.0616` n `20`; unknown avg `0.538` n `773`
- 4h: commodity avg `0.1111` n `12`; crypto_alt avg `0.2046` n `230`; crypto_major avg `0.1564` n `8`; equity avg `-0.2411` n `98`; fx avg `-0.0059` n `6`; index avg `-0.0406` n `25`; metal avg `0.0898` n `20`; unknown avg `0.5876` n `773`
- 24h: commodity avg `0.7475` n `12`; crypto_alt avg `-0.676` n `230`; crypto_major avg `-1.408` n `8`; equity avg `0.1911` n `98`; fx avg `-0.0144` n `6`; index avg `-0.0862` n `25`; metal avg `0.3762` n `20`; unknown avg `0.6411` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1046`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.087`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0759`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0725`, n `666`, weak_sample_signal
