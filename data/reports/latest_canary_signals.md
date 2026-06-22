# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T09:22:32.840576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.122` n `228`; crypto_major avg `-0.0961` n `8`; equity avg `-0.0321` n `79`; fx avg `0.0078` n `6`; index avg `-0.0025` n `23`; metal avg `-0.0206` n `18`; unknown avg `0.0046` n `701`
- 1h: commodity avg `-0.1776` n `12`; crypto_alt avg `-0.0473` n `228`; crypto_major avg `-0.2048` n `8`; equity avg `0.1574` n `79`; fx avg `0.0258` n `6`; index avg `0.0333` n `23`; metal avg `0.1884` n `18`; unknown avg `-0.051` n `701`
- 4h: commodity avg `0.077` n `12`; crypto_alt avg `-0.0028` n `228`; crypto_major avg `0.1982` n `8`; equity avg `0.35` n `79`; fx avg `0.035` n `6`; index avg `0.0594` n `23`; metal avg `0.3019` n `18`; unknown avg `0.2282` n `661`
- 24h: commodity avg `-0.2431` n `12`; crypto_alt avg `-0.0241` n `228`; crypto_major avg `0.0945` n `8`; equity avg `-0.1631` n `79`; fx avg `0.0423` n `6`; index avg `0.0349` n `23`; metal avg `0.4805` n `18`; unknown avg `0.142` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
