# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T01:07:32.709975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.21` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `3.6787` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0466` n `12`; crypto_alt avg `-0.209` n `228`; crypto_major avg `-0.2423` n `8`; equity avg `-0.0095` n `74`; fx avg `0.0098` n `6`; index avg `-0.0906` n `23`; metal avg `-0.0564` n `18`; unknown avg `1.7889` n `645`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.5231` n `228`; crypto_major avg `-0.4581` n `8`; equity avg `0.0238` n `74`; fx avg `0.0408` n `6`; index avg `0.1467` n `23`; metal avg `-0.0615` n `18`; unknown avg `0.4087` n `645`
- 4h: commodity avg `-0.9828` n `12`; crypto_alt avg `2.3548` n `228`; crypto_major avg `2.6959` n `8`; equity avg `1.3406` n `74`; fx avg `0.0091` n `6`; index avg `0.5293` n `23`; metal avg `1.7348` n `18`; unknown avg `2.251` n `637`
- 24h: commodity avg `-0.8323` n `12`; crypto_alt avg `1.5589` n `228`; crypto_major avg `1.8374` n `8`; equity avg `1.5546` n `74`; fx avg `-0.0078` n `6`; index avg `0.6666` n `23`; metal avg `1.6172` n `18`; unknown avg `1.6794` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
