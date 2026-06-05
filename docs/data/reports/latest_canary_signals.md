# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T12:22:23.362548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0808` n `12`; crypto_alt avg `-0.0641` n `228`; crypto_major avg `-0.0738` n `8`; equity avg `0.0069` n `74`; fx avg `0.0079` n `6`; index avg `0.021` n `23`; metal avg `0.235` n `18`; unknown avg `-0.1698` n `424`
- 1h: commodity avg `-0.2216` n `12`; crypto_alt avg `-0.7738` n `228`; crypto_major avg `-0.7968` n `8`; equity avg `-0.2587` n `74`; fx avg `0.0228` n `6`; index avg `-0.0662` n `23`; metal avg `0.5316` n `18`; unknown avg `2.1852` n `424`
- 4h: commodity avg `0.0037` n `12`; crypto_alt avg `-0.1836` n `228`; crypto_major avg `-0.0801` n `8`; equity avg `-0.0331` n `74`; fx avg `0.0524` n `6`; index avg `-0.0095` n `23`; metal avg `0.6784` n `18`; unknown avg `2.3113` n `424`
- 24h: commodity avg `-0.1697` n `12`; crypto_alt avg `-4.5117` n `228`; crypto_major avg `-3.2047` n `8`; equity avg `-0.3194` n `74`; fx avg `0.1329` n `6`; index avg `0.0706` n `23`; metal avg `-0.5517` n `18`; unknown avg `0.1596` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
