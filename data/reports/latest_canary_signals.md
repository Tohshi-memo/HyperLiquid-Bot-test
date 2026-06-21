# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T14:30:55.210017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0288` n `12`; crypto_alt avg `0.0265` n `228`; crypto_major avg `-0.0074` n `8`; equity avg `-0.013` n `78`; fx avg `-0.0021` n `6`; index avg `-0.0058` n `23`; metal avg `0.0035` n `18`; unknown avg `-0.0066` n `702`
- 1h: commodity avg `0.0593` n `12`; crypto_alt avg `0.0059` n `228`; crypto_major avg `0.0741` n `8`; equity avg `-0.0317` n `78`; fx avg `0.0189` n `6`; index avg `-0.0131` n `23`; metal avg `-0.0168` n `18`; unknown avg `-0.0607` n `702`
- 4h: commodity avg `0.1389` n `12`; crypto_alt avg `-0.186` n `228`; crypto_major avg `-0.5017` n `8`; equity avg `-0.0967` n `78`; fx avg `0.0428` n `6`; index avg `-0.0126` n `23`; metal avg `-0.0681` n `18`; unknown avg `0.135` n `702`
- 24h: commodity avg `-0.055` n `12`; crypto_alt avg `2.2724` n `228`; crypto_major avg `0.5489` n `8`; equity avg `0.5412` n `78`; fx avg `0.0485` n `6`; index avg `0.044` n `23`; metal avg `-0.0243` n `18`; unknown avg `1.3053` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
