# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T14:22:34.141509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `0.0571` n `233`; crypto_major avg `-0.0152` n `8`; equity avg `-0.074` n `136`; fx avg `-0.0105` n `6`; index avg `-0.0441` n `27`; metal avg `-0.0095` n `20`; unknown avg `0.5343` n `894`
- 1h: commodity avg `0.0939` n `12`; crypto_alt avg `0.3435` n `233`; crypto_major avg `0.4138` n `8`; equity avg `0.7084` n `136`; fx avg `-0.0177` n `6`; index avg `0.0146` n `27`; metal avg `-0.0955` n `20`; unknown avg `1.1465` n `878`
- 4h: commodity avg `0.1639` n `12`; crypto_alt avg `-0.2766` n `233`; crypto_major avg `0.0114` n `8`; equity avg `0.2775` n `136`; fx avg `0.0468` n `6`; index avg `0.0036` n `27`; metal avg `-0.0615` n `20`; unknown avg `1.081` n `872`
- 24h: commodity avg `0.7348` n `12`; crypto_alt avg `-0.8839` n `233`; crypto_major avg `1.3538` n `8`; equity avg `-0.7208` n `136`; fx avg `0.0634` n `6`; index avg `-0.2764` n `27`; metal avg `-0.5547` n `20`; unknown avg `1.3066` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
