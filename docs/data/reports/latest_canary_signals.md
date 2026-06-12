# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T10:47:56.306198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1789` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.022` n `228`; crypto_major avg `0.1011` n `8`; equity avg `-0.0315` n `74`; fx avg `-0.0032` n `6`; index avg `0.0108` n `23`; metal avg `0.0269` n `18`; unknown avg `0.184` n `643`
- 1h: commodity avg `0.2739` n `12`; crypto_alt avg `-0.2625` n `228`; crypto_major avg `-0.3188` n `8`; equity avg `-0.2792` n `74`; fx avg `0.0099` n `6`; index avg `-0.1234` n `23`; metal avg `-0.2699` n `18`; unknown avg `1.2011` n `643`
- 4h: commodity avg `-0.8023` n `12`; crypto_alt avg `1.5445` n `228`; crypto_major avg `1.3766` n `8`; equity avg `0.8477` n `74`; fx avg `0.0093` n `6`; index avg `0.3969` n `23`; metal avg `0.6169` n `18`; unknown avg `0.7414` n `531`
- 24h: commodity avg `-2.1229` n `12`; crypto_alt avg `1.9885` n `228`; crypto_major avg `1.8372` n `8`; equity avg `2.627` n `74`; fx avg `0.0394` n `6`; index avg `1.4358` n `23`; metal avg `3.1573` n `18`; unknown avg `1.5091` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
