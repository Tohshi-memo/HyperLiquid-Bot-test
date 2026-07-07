# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T18:37:29.472818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `0.0017` n `229`; crypto_major avg `-0.0853` n `8`; equity avg `-0.2599` n `91`; fx avg `-0.0051` n `6`; index avg `-0.023` n `25`; metal avg `-0.0195` n `20`; unknown avg `-0.0837` n `763`
- 1h: commodity avg `-0.111` n `12`; crypto_alt avg `-0.2443` n `229`; crypto_major avg `-0.2852` n `8`; equity avg `-0.3416` n `91`; fx avg `-0.02` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0413` n `20`; unknown avg `1.0562` n `763`
- 4h: commodity avg `-0.0245` n `12`; crypto_alt avg `1.0467` n `229`; crypto_major avg `1.3906` n `8`; equity avg `0.9938` n `91`; fx avg `-0.0642` n `6`; index avg `0.2002` n `25`; metal avg `0.0576` n `20`; unknown avg `0.1436` n `755`
- 24h: commodity avg `0.4946` n `12`; crypto_alt avg `-1.1721` n `229`; crypto_major avg `-0.3775` n `8`; equity avg `-2.783` n `91`; fx avg `-0.2668` n `6`; index avg `-0.505` n `25`; metal avg `-0.2821` n `20`; unknown avg `-0.4119` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
