# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T12:52:28.797567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0572` n `230`; crypto_major avg `-0.0207` n `8`; equity avg `-0.0458` n `98`; fx avg `-0.0051` n `6`; index avg `-0.0257` n `25`; metal avg `-0.0576` n `20`; unknown avg `-0.0101` n `773`
- 1h: commodity avg `-0.1087` n `12`; crypto_alt avg `-0.2496` n `230`; crypto_major avg `-0.2567` n `8`; equity avg `-0.1487` n `98`; fx avg `0.0033` n `6`; index avg `-0.0275` n `25`; metal avg `0.0053` n `20`; unknown avg `-0.0132` n `773`
- 4h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.0469` n `230`; crypto_major avg `-0.0817` n `8`; equity avg `-0.3191` n `98`; fx avg `-0.0007` n `6`; index avg `-0.0629` n `25`; metal avg `0.0997` n `20`; unknown avg `0.4639` n `773`
- 24h: commodity avg `0.5271` n `12`; crypto_alt avg `-0.898` n `230`; crypto_major avg `-1.6806` n `8`; equity avg `0.0858` n `98`; fx avg `-0.0048` n `6`; index avg `-0.097` n `25`; metal avg `0.3877` n `20`; unknown avg `0.4972` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1038`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0918`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0798`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
