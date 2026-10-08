# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T03:07:26.474710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `13`; crypto_alt avg `-0.5037` n `235`; crypto_major avg `-0.3572` n `8`; equity avg `-0.2418` n `150`; fx avg `0.0082` n `6`; index avg `-0.0408` n `26`; metal avg `-0.0655` n `20`; unknown avg `0.0332` n `1075`
- 1h: commodity avg `0.0516` n `13`; crypto_alt avg `-0.2273` n `235`; crypto_major avg `-0.1957` n `8`; equity avg `-0.2804` n `150`; fx avg `0.0293` n `6`; index avg `-0.0362` n `26`; metal avg `-0.0367` n `20`; unknown avg `-0.1349` n `1075`
- 4h: commodity avg `0.206` n `13`; crypto_alt avg `0.0881` n `235`; crypto_major avg `-0.0439` n `8`; equity avg `-0.3499` n `150`; fx avg `-0.0054` n `6`; index avg `-0.0605` n `26`; metal avg `0.3254` n `20`; unknown avg `-0.3165` n `1069`
- 24h: commodity avg `0.458` n `13`; crypto_alt avg `-0.9144` n `235`; crypto_major avg `-1.612` n `8`; equity avg `-1.08` n `150`; fx avg `-0.1399` n `6`; index avg `-0.2088` n `26`; metal avg `-0.1777` n `20`; unknown avg `247.0522` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1522`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1327`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1028`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0915`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0898`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.07`, n `669`, weak_sample_signal
