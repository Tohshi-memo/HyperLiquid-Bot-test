# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T22:22:28.757035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1431` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2041` n `12`; crypto_alt avg `0.3403` n `228`; crypto_major avg `0.2847` n `8`; equity avg `-0.0273` n `74`; fx avg `0.0195` n `6`; index avg `-0.0207` n `23`; metal avg `0.0289` n `18`; unknown avg `0.1107` n `547`
- 1h: commodity avg `-0.0484` n `12`; crypto_alt avg `-0.0697` n `228`; crypto_major avg `-0.21` n `8`; equity avg `-0.0932` n `74`; fx avg `-0.0195` n `6`; index avg `0.014` n `23`; metal avg `-0.0971` n `18`; unknown avg `-0.0802` n `547`
- 4h: commodity avg `0.262` n `12`; crypto_alt avg `-0.0295` n `228`; crypto_major avg `-0.3316` n `8`; equity avg `0.2467` n `74`; fx avg `-0.0436` n `6`; index avg `0.8115` n `23`; metal avg `-0.1957` n `18`; unknown avg `0.051` n `547`
- 24h: commodity avg `-0.7409` n `12`; crypto_alt avg `-1.6932` n `228`; crypto_major avg `-2.8742` n `8`; equity avg `-1.9086` n `74`; fx avg `0.071` n `6`; index avg `-0.7893` n `23`; metal avg `-1.4437` n `18`; unknown avg `-1.0833` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.04`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.038`, n `668`, weak_sample_signal
