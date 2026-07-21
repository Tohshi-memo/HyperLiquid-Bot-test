# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T02:52:32.095481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0025` n `230`; crypto_major avg `-0.0076` n `8`; equity avg `0.082` n `98`; fx avg `-0.0202` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0215` n `20`; unknown avg `-0.1094` n `771`
- 1h: commodity avg `0.0093` n `12`; crypto_alt avg `0.0447` n `230`; crypto_major avg `0.1349` n `8`; equity avg `0.2051` n `98`; fx avg `-0.0173` n `6`; index avg `0.0486` n `25`; metal avg `0.1146` n `20`; unknown avg `-0.2149` n `771`
- 4h: commodity avg `-0.0433` n `12`; crypto_alt avg `0.4151` n `230`; crypto_major avg `0.5119` n `8`; equity avg `0.4821` n `98`; fx avg `0.0444` n `6`; index avg `0.2161` n `25`; metal avg `0.2967` n `20`; unknown avg `-0.5653` n `770`
- 24h: commodity avg `-0.2984` n `12`; crypto_alt avg `1.1918` n `230`; crypto_major avg `0.9948` n `8`; equity avg `0.0516` n `98`; fx avg `-0.111` n `6`; index avg `0.0893` n `25`; metal avg `0.1686` n `20`; unknown avg `-0.1229` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0838`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
