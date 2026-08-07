# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T22:52:32.354391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `0.0677` n `230`; crypto_major avg `0.0488` n `8`; equity avg `0.0332` n `112`; fx avg `0.0038` n `6`; index avg `-0.0043` n `25`; metal avg `0.0044` n `20`; unknown avg `0.0271` n `782`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `-0.0984` n `230`; crypto_major avg `-0.0804` n `8`; equity avg `0.0593` n `112`; fx avg `0.015` n `6`; index avg `0.0075` n `25`; metal avg `0.0586` n `20`; unknown avg `0.0703` n `782`
- 4h: commodity avg `-0.2855` n `12`; crypto_alt avg `-0.1098` n `230`; crypto_major avg `0.316` n `8`; equity avg `0.5783` n `112`; fx avg `0.0218` n `6`; index avg `0.0839` n `25`; metal avg `0.097` n `20`; unknown avg `-0.1058` n `782`
- 24h: commodity avg `-0.1794` n `12`; crypto_alt avg `-0.421` n `230`; crypto_major avg `-0.1875` n `8`; equity avg `1.664` n `112`; fx avg `-0.1173` n `6`; index avg `0.079` n `25`; metal avg `0.4939` n `20`; unknown avg `0.0936` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
