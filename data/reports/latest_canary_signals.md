# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T08:37:38.536345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3724` n `13`; crypto_alt avg `-0.2607` n `235`; crypto_major avg `-0.0557` n `8`; equity avg `-0.1757` n `144`; fx avg `0.0383` n `6`; index avg `-0.0507` n `26`; metal avg `-0.0531` n `20`; unknown avg `0.6626` n `1079`
- 1h: commodity avg `0.2567` n `13`; crypto_alt avg `-0.0691` n `235`; crypto_major avg `0.1749` n `8`; equity avg `0.0057` n `144`; fx avg `0.0474` n `6`; index avg `-0.0097` n `26`; metal avg `0.1288` n `20`; unknown avg `-0.0232` n `997`
- 4h: commodity avg `0.3074` n `13`; crypto_alt avg `1.2595` n `235`; crypto_major avg `1.1053` n `8`; equity avg `0.0586` n `144`; fx avg `0.0375` n `6`; index avg `-0.0039` n `26`; metal avg `0.2817` n `20`; unknown avg `-0.35` n `981`
- 24h: commodity avg `0.0275` n `13`; crypto_alt avg `0.7596` n `235`; crypto_major avg `1.4553` n `8`; equity avg `0.2779` n `144`; fx avg `-0.0282` n `6`; index avg `-0.0509` n `26`; metal avg `0.2977` n `20`; unknown avg `-0.3684` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
