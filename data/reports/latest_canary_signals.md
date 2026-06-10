# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T10:07:33.376825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0839` n `12`; crypto_alt avg `-0.0051` n `228`; crypto_major avg `-0.1222` n `8`; equity avg `-0.0617` n `74`; fx avg `-0.0` n `6`; index avg `-0.0` n `23`; metal avg `-0.0621` n `18`; unknown avg `-0.1069` n `547`
- 1h: commodity avg `0.4075` n `12`; crypto_alt avg `-0.0927` n `228`; crypto_major avg `-0.1369` n `8`; equity avg `0.0209` n `74`; fx avg `0.0049` n `6`; index avg `0.0155` n `23`; metal avg `-0.1321` n `18`; unknown avg `0.0742` n `547`
- 4h: commodity avg `0.5048` n `12`; crypto_alt avg `0.0377` n `228`; crypto_major avg `-0.2932` n `8`; equity avg `-0.6572` n `74`; fx avg `0.0058` n `6`; index avg `-0.3279` n `23`; metal avg `-0.8146` n `18`; unknown avg `-0.2144` n `547`
- 24h: commodity avg `-0.4155` n `12`; crypto_alt avg `-1.2806` n `228`; crypto_major avg `-3.6668` n `8`; equity avg `-4.3042` n `74`; fx avg `0.0308` n `6`; index avg `-2.3626` n `23`; metal avg `-3.4349` n `18`; unknown avg `0.2785` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
