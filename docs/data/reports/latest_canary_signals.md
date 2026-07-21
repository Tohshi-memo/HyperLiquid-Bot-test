# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T22:22:25.374443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.054` n `230`; crypto_major avg `-0.0152` n `8`; equity avg `0.052` n `98`; fx avg `0.0001` n `6`; index avg `0.0043` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0751` n `771`
- 1h: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.0949` n `230`; crypto_major avg `-0.1394` n `8`; equity avg `-0.0691` n `98`; fx avg `0.0003` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0089` n `20`; unknown avg `-0.0912` n `771`
- 4h: commodity avg `0.1348` n `12`; crypto_alt avg `0.0199` n `230`; crypto_major avg `-0.1698` n `8`; equity avg `0.5618` n `98`; fx avg `-0.004` n `6`; index avg `0.0103` n `25`; metal avg `0.0188` n `20`; unknown avg `-0.1722` n `771`
- 24h: commodity avg `0.4586` n `12`; crypto_alt avg `0.9513` n `230`; crypto_major avg `0.6987` n `8`; equity avg `4.4445` n `98`; fx avg `0.0651` n `6`; index avg `0.6895` n `25`; metal avg `0.7785` n `20`; unknown avg `0.1837` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0938`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0555`, n `666`, weak_sample_signal
