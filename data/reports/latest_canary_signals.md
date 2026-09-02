# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T19:22:28.386679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0211` n `12`; crypto_alt avg `-0.0422` n `232`; crypto_major avg `-0.009` n `8`; equity avg `0.0562` n `133`; fx avg `0.0028` n `6`; index avg `0.009` n `26`; metal avg `0.024` n `20`; unknown avg `-0.1456` n `792`
- 1h: commodity avg `0.0438` n `12`; crypto_alt avg `-0.0138` n `232`; crypto_major avg `-0.0249` n `8`; equity avg `0.144` n `133`; fx avg `0.0118` n `6`; index avg `-0.001` n `26`; metal avg `0.0341` n `20`; unknown avg `-0.5914` n `790`
- 4h: commodity avg `0.0638` n `12`; crypto_alt avg `0.4621` n `232`; crypto_major avg `0.3982` n `8`; equity avg `0.8675` n `133`; fx avg `0.0242` n `6`; index avg `0.0496` n `26`; metal avg `0.0562` n `20`; unknown avg `15.3223` n `790`
- 24h: commodity avg `0.2214` n `12`; crypto_alt avg `-0.307` n `232`; crypto_major avg `-0.3912` n `8`; equity avg `0.7285` n `133`; fx avg `-0.3402` n `6`; index avg `0.1296` n `26`; metal avg `0.4266` n `20`; unknown avg `-0.3386` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0423`, n `668`, weak_sample_signal
