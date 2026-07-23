# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T23:07:24.174552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `0.1057` n `8`; equity avg `-0.0228` n `100`; fx avg `-0.0009` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0266` n `20`; unknown avg `0.0111` n `772`
- 1h: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.0955` n `230`; crypto_major avg `0.0619` n `8`; equity avg `0.0039` n `100`; fx avg `0.0055` n `6`; index avg `0.019` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.1295` n `772`
- 4h: commodity avg `0.0505` n `12`; crypto_alt avg `-0.0622` n `230`; crypto_major avg `0.1345` n `8`; equity avg `0.3629` n `100`; fx avg `0.0055` n `6`; index avg `0.1073` n `25`; metal avg `0.0407` n `20`; unknown avg `0.2043` n `772`
- 24h: commodity avg `0.6614` n `12`; crypto_alt avg `-1.6038` n `230`; crypto_major avg `-2.084` n `8`; equity avg `-1.0787` n `99`; fx avg `-0.0563` n `6`; index avg `-0.1925` n `25`; metal avg `-0.6475` n `20`; unknown avg `-0.2973` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
