# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T18:00:17.956076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0562` n `228`; crypto_major avg `-0.0246` n `8`; equity avg `-0.0011` n `78`; fx avg `0.0132` n `6`; index avg `-0.0123` n `23`; metal avg `-0.0476` n `18`; unknown avg `-0.2106` n `702`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.2944` n `228`; crypto_major avg `-0.2015` n `8`; equity avg `-0.0268` n `78`; fx avg `0.0054` n `6`; index avg `-0.0242` n `23`; metal avg `-0.0245` n `18`; unknown avg `0.3789` n `702`
- 4h: commodity avg `0.1643` n `12`; crypto_alt avg `-0.0101` n `228`; crypto_major avg `0.1415` n `8`; equity avg `0.0173` n `78`; fx avg `-0.0808` n `6`; index avg `-0.0331` n `23`; metal avg `-0.0403` n `18`; unknown avg `-0.8772` n `702`
- 24h: commodity avg `0.1328` n `12`; crypto_alt avg `1.3987` n `228`; crypto_major avg `0.3448` n `8`; equity avg `0.4476` n `78`; fx avg `-0.0654` n `6`; index avg `0.0211` n `23`; metal avg `-0.0308` n `18`; unknown avg `-0.4133` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
