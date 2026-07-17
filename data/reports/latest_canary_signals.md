# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T14:52:37.972029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0517` n `12`; crypto_alt avg `-0.2061` n `230`; crypto_major avg `-0.1352` n `8`; equity avg `-0.3006` n `96`; fx avg `0.0068` n `6`; index avg `-0.0526` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.0422` n `769`
- 1h: commodity avg `-0.127` n `12`; crypto_alt avg `0.4198` n `230`; crypto_major avg `0.416` n `8`; equity avg `1.3886` n `96`; fx avg `0.0082` n `6`; index avg `0.1869` n `25`; metal avg `0.0987` n `20`; unknown avg `0.0349` n `769`
- 4h: commodity avg `0.235` n `12`; crypto_alt avg `-0.2407` n `230`; crypto_major avg `-0.2987` n `8`; equity avg `0.2528` n `96`; fx avg `0.0267` n `6`; index avg `-0.0039` n `25`; metal avg `0.0506` n `20`; unknown avg `0.268` n `769`
- 24h: commodity avg `0.3777` n `12`; crypto_alt avg `-2.1939` n `230`; crypto_major avg `-3.2023` n `8`; equity avg `-2.6732` n `94`; fx avg `-0.0165` n `6`; index avg `-0.4972` n `25`; metal avg `-0.4331` n `20`; unknown avg `-0.419` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
