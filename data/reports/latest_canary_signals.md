# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T09:21:05.531951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `0.1245` n `8`; equity avg `0.0202` n `100`; fx avg `-0.0008` n `6`; index avg `0.0169` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0103` n `774`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.1172` n `230`; crypto_major avg `-0.0108` n `8`; equity avg `-0.0354` n `100`; fx avg `0.0081` n `6`; index avg `0.0188` n `25`; metal avg `0.0046` n `20`; unknown avg `0.3419` n `774`
- 4h: commodity avg `0.0727` n `12`; crypto_alt avg `-0.4978` n `230`; crypto_major avg `-0.3054` n `8`; equity avg `-0.0898` n `100`; fx avg `0.0334` n `6`; index avg `0.0025` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.243` n `758`
- 24h: commodity avg `0.1371` n `12`; crypto_alt avg `-1.6472` n `230`; crypto_major avg `-1.286` n `8`; equity avg `-2.859` n `100`; fx avg `0.0002` n `6`; index avg `-0.2456` n `25`; metal avg `-0.0983` n `20`; unknown avg `13.3207` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1158`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1002`, n `666`, weak_sample_signal
