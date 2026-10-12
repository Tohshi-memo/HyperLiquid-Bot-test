# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T02:37:24.021118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `0.1901` n `235`; crypto_major avg `0.0648` n `8`; equity avg `-0.5165` n `151`; fx avg `-0.0117` n `6`; index avg `0.0028` n `26`; metal avg `-0.0241` n `20`; unknown avg `-0.1` n `1113`
- 1h: commodity avg `-0.0695` n `13`; crypto_alt avg `0.622` n `235`; crypto_major avg `0.3523` n `8`; equity avg `-0.4595` n `151`; fx avg `-0.0317` n `6`; index avg `0.025` n `26`; metal avg `0.0655` n `20`; unknown avg `0.6078` n `1111`
- 4h: commodity avg `-0.5709` n `13`; crypto_alt avg `0.3213` n `235`; crypto_major avg `0.4088` n `8`; equity avg `-0.5255` n `151`; fx avg `-0.057` n `6`; index avg `-0.0168` n `26`; metal avg `0.1712` n `20`; unknown avg `2.3957` n `1089`
- 24h: commodity avg `-0.3977` n `13`; crypto_alt avg `1.8749` n `235`; crypto_major avg `1.0442` n `8`; equity avg `-0.2166` n `151`; fx avg `-0.0591` n `6`; index avg `0.0239` n `26`; metal avg `0.1983` n `20`; unknown avg `0.7624` n `928`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
