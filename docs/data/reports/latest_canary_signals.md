# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T00:37:25.457842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-1.7517` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2248` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `-1.2933` n `228`; crypto_major avg `-1.1189` n `8`; equity avg `0.3309` n `73`; fx avg `0.0454` n `6`; index avg `0.1308` n `23`; metal avg `-0.0533` n `18`; unknown avg `-0.5078` n `419`
- 1h: commodity avg `-0.0255` n `12`; crypto_alt avg `-1.0422` n `228`; crypto_major avg `-1.0792` n `8`; equity avg `0.6725` n `73`; fx avg `-0.02` n `6`; index avg `0.1456` n `23`; metal avg `-0.0907` n `18`; unknown avg `-0.5539` n `419`
- 4h: commodity avg `-0.2577` n `12`; crypto_alt avg `-0.9039` n `228`; crypto_major avg `-0.8595` n `8`; equity avg `-0.5263` n `73`; fx avg `-0.0635` n `6`; index avg `-0.1911` n `23`; metal avg `0.2323` n `18`; unknown avg `-0.0039` n `419`
- 24h: commodity avg `0.2926` n `12`; crypto_alt avg `-0.0238` n `228`; crypto_major avg `-2.8039` n `8`; equity avg `-3.2165` n `72`; fx avg `0.026` n `6`; index avg `-1.075` n `23`; metal avg `-2.0215` n `18`; unknown avg `0.4391` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
