# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T04:37:25.531227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `0.0107` n `228`; crypto_major avg `-0.0809` n `8`; equity avg `0.1076` n `74`; fx avg `-0.0087` n `6`; index avg `0.0343` n `23`; metal avg `-0.0358` n `18`; unknown avg `-0.0519` n `550`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.7995` n `228`; crypto_major avg `0.2643` n `8`; equity avg `0.3753` n `74`; fx avg `0.0045` n `6`; index avg `0.2538` n `23`; metal avg `0.2326` n `18`; unknown avg `11.6314` n `550`
- 4h: commodity avg `-0.1618` n `12`; crypto_alt avg `1.8658` n `228`; crypto_major avg `1.4478` n `8`; equity avg `0.987` n `74`; fx avg `0.044` n `6`; index avg `0.6892` n `23`; metal avg `0.613` n `18`; unknown avg `2.599` n `550`
- 24h: commodity avg `1.5515` n `12`; crypto_alt avg `1.3916` n `228`; crypto_major avg `0.8109` n `8`; equity avg `0.1392` n `74`; fx avg `0.0289` n `6`; index avg `-0.3981` n `23`; metal avg `-0.2855` n `18`; unknown avg `2.8487` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
