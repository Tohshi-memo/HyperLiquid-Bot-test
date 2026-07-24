# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T04:37:27.895874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.0181` n `230`; crypto_major avg `0.0379` n `8`; equity avg `0.1335` n `100`; fx avg `0.0073` n `6`; index avg `0.0235` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.1054` n `772`
- 1h: commodity avg `-0.0672` n `12`; crypto_alt avg `-0.0135` n `230`; crypto_major avg `-0.0593` n `8`; equity avg `0.0669` n `100`; fx avg `0.0065` n `6`; index avg `0.0088` n `25`; metal avg `-0.0127` n `20`; unknown avg `0.0665` n `772`
- 4h: commodity avg `-0.022` n `12`; crypto_alt avg `0.7132` n `230`; crypto_major avg `0.4611` n `8`; equity avg `-0.3543` n `100`; fx avg `-0.0616` n `6`; index avg `-0.1183` n `25`; metal avg `-0.1985` n `20`; unknown avg `0.8213` n `772`
- 24h: commodity avg `0.5823` n `12`; crypto_alt avg `-1.0976` n `230`; crypto_major avg `-1.758` n `8`; equity avg `-2.1921` n `99`; fx avg `-0.1058` n `6`; index avg `-0.6183` n `25`; metal avg `-1.0713` n `20`; unknown avg `-0.2606` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1106`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0979`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0928`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
