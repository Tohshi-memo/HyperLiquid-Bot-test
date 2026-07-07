# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T17:07:27.887779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5988` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0321` n `12`; crypto_alt avg `-0.1045` n `229`; crypto_major avg `-0.1513` n `8`; equity avg `0.0672` n `91`; fx avg `0.004` n `6`; index avg `0.0139` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0229` n `763`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.1537` n `229`; crypto_major avg `0.222` n `8`; equity avg `0.5184` n `91`; fx avg `-0.0055` n `6`; index avg `0.0903` n `25`; metal avg `0.0833` n `20`; unknown avg `0.0764` n `763`
- 4h: commodity avg `0.5197` n `12`; crypto_alt avg `0.3252` n `229`; crypto_major avg `0.8608` n `8`; equity avg `-0.738` n `91`; fx avg `-0.0382` n `6`; index avg `-0.0731` n `25`; metal avg `-0.1311` n `20`; unknown avg `0.1721` n `755`
- 24h: commodity avg `0.7079` n `12`; crypto_alt avg `-0.777` n `229`; crypto_major avg `-0.2756` n `8`; equity avg `-2.9623` n `91`; fx avg `-0.2542` n `6`; index avg `-0.5447` n `25`; metal avg `-0.1209` n `20`; unknown avg `-0.0582` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
