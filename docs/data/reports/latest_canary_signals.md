# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T12:22:40.004824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0597` n `13`; crypto_alt avg `-0.0542` n `235`; crypto_major avg `-0.0554` n `8`; equity avg `-0.0235` n `144`; fx avg `-0.0231` n `6`; index avg `-0.0008` n `26`; metal avg `0.0039` n `20`; unknown avg `0.1478` n `1079`
- 1h: commodity avg `0.0744` n `13`; crypto_alt avg `0.0278` n `235`; crypto_major avg `-0.0766` n `8`; equity avg `-0.0336` n `144`; fx avg `-0.0146` n `6`; index avg `0.013` n `26`; metal avg `0.003` n `20`; unknown avg `1.5993` n `1071`
- 4h: commodity avg `0.2123` n `13`; crypto_alt avg `-0.3648` n `235`; crypto_major avg `-0.4607` n `8`; equity avg `-0.3337` n `144`; fx avg `0.0281` n `6`; index avg `-0.0272` n `26`; metal avg `-0.0587` n `20`; unknown avg `44.9902` n `1071`
- 24h: commodity avg `-0.1632` n `13`; crypto_alt avg `1.1905` n `235`; crypto_major avg `0.8755` n `8`; equity avg `0.0733` n `144`; fx avg `-0.0658` n `6`; index avg `-0.0411` n `26`; metal avg `0.299` n `20`; unknown avg `0.8109` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
