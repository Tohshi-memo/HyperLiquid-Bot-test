# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T03:37:31.102541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1328` n `12`; crypto_alt avg `0.0948` n `228`; crypto_major avg `0.1015` n `8`; equity avg `0.09` n `74`; fx avg `0.009` n `6`; index avg `0.1125` n `23`; metal avg `0.0243` n `18`; unknown avg `0.3902` n `557`
- 1h: commodity avg `-0.08` n `12`; crypto_alt avg `-0.1771` n `228`; crypto_major avg `-0.1542` n `8`; equity avg `0.0459` n `74`; fx avg `0.0101` n `6`; index avg `0.0271` n `23`; metal avg `0.3358` n `18`; unknown avg `-0.2541` n `557`
- 4h: commodity avg `0.4086` n `12`; crypto_alt avg `0.2534` n `228`; crypto_major avg `-0.0203` n `8`; equity avg `0.1578` n `74`; fx avg `0.0347` n `6`; index avg `-0.086` n `23`; metal avg `0.0979` n `18`; unknown avg `-0.1858` n `556`
- 24h: commodity avg `-2.4318` n `12`; crypto_alt avg `2.7588` n `228`; crypto_major avg `2.7564` n `8`; equity avg `4.0913` n `74`; fx avg `0.0265` n `6`; index avg `2.1372` n `23`; metal avg `3.6209` n `18`; unknown avg `1.9091` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
