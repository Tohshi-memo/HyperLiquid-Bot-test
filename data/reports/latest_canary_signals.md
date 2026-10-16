# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T04:37:29.724043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `13`; crypto_alt avg `-0.1133` n `236`; crypto_major avg `-0.0789` n `8`; equity avg `0.0108` n `151`; fx avg `-0.0109` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0273` n `20`; unknown avg `0.0138` n `1134`
- 1h: commodity avg `0.0894` n `13`; crypto_alt avg `0.9028` n `236`; crypto_major avg `0.4317` n `8`; equity avg `0.6504` n `151`; fx avg `0.0345` n `6`; index avg `0.0968` n `26`; metal avg `0.1054` n `20`; unknown avg `0.7771` n `1124`
- 4h: commodity avg `-0.029` n `13`; crypto_alt avg `-0.1646` n `236`; crypto_major avg `-0.3032` n `8`; equity avg `0.9387` n `151`; fx avg `0.0288` n `6`; index avg `0.1292` n `26`; metal avg `0.3106` n `20`; unknown avg `0.3624` n `1124`
- 24h: commodity avg `0.0457` n `13`; crypto_alt avg `2.6639` n `236`; crypto_major avg `1.0558` n `8`; equity avg `2.2396` n `151`; fx avg `0.0587` n `6`; index avg `0.3472` n `26`; metal avg `0.5169` n `20`; unknown avg `25.6619` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1026`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0706`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0631`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
