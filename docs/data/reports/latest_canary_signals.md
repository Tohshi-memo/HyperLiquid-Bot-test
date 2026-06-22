# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T03:07:27.838350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `-0.3627` n `228`; crypto_major avg `-0.6204` n `8`; equity avg `-0.1062` n `79`; fx avg `-0.0036` n `6`; index avg `-0.008` n `23`; metal avg `-0.0394` n `18`; unknown avg `1.3676` n `701`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `-0.5786` n `228`; crypto_major avg `-0.8392` n `8`; equity avg `-0.3578` n `79`; fx avg `0.0095` n `6`; index avg `-0.061` n `23`; metal avg `-0.1583` n `18`; unknown avg `0.8679` n `701`
- 4h: commodity avg `-0.3674` n `12`; crypto_alt avg `0.7135` n `228`; crypto_major avg `0.3856` n `8`; equity avg `-0.2489` n `79`; fx avg `0.135` n `6`; index avg `0.1056` n `23`; metal avg `0.1887` n `18`; unknown avg `-0.0548` n `685`
- 24h: commodity avg `-0.2634` n `12`; crypto_alt avg `0.0007` n `228`; crypto_major avg `-0.8224` n `8`; equity avg `-0.5583` n `79`; fx avg `0.02` n `6`; index avg `0.0017` n `23`; metal avg `0.1396` n `18`; unknown avg `0.0673` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
