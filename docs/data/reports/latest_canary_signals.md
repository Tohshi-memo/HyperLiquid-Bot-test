# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T14:26:08.323846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.5922` n `229`; crypto_major avg `-0.5839` n `8`; equity avg `-0.9737` n `88`; fx avg `0.0157` n `6`; index avg `-0.1511` n `25`; metal avg `-0.1529` n `20`; unknown avg `0.1342` n `763`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.3073` n `229`; crypto_major avg `-0.0856` n `8`; equity avg `-0.435` n `88`; fx avg `-0.0064` n `6`; index avg `-0.0771` n `25`; metal avg `0.0894` n `20`; unknown avg `0.0747` n `763`
- 4h: commodity avg `-0.0108` n `12`; crypto_alt avg `0.4988` n `229`; crypto_major avg `1.4332` n `8`; equity avg `0.8155` n `88`; fx avg `0.0292` n `6`; index avg `0.1596` n `25`; metal avg `0.5195` n `20`; unknown avg `-0.455` n `763`
- 24h: commodity avg `-0.3691` n `12`; crypto_alt avg `1.9329` n `228`; crypto_major avg `2.9209` n `8`; equity avg `-1.3852` n `88`; fx avg `-0.033` n `6`; index avg `-0.3393` n `25`; metal avg `0.358` n `20`; unknown avg `1.355` n `739`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
