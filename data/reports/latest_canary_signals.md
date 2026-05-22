# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T07:52:17.969846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `0.0894` n `228`; crypto_major avg `0.0461` n `8`; equity avg `0.0374` n `67`; fx avg `0.0069` n `6`; index avg `0.0239` n `23`; metal avg `-0.0028` n `18`; unknown avg `1.1901` n `386`
- 1h: commodity avg `0.1684` n `12`; crypto_alt avg `0.3405` n `228`; crypto_major avg `0.2689` n `8`; equity avg `-0.0657` n `67`; fx avg `-0.0179` n `6`; index avg `-0.0377` n `23`; metal avg `-0.2874` n `18`; unknown avg `1.0674` n `386`
- 4h: commodity avg `0.5218` n `12`; crypto_alt avg `0.1692` n `228`; crypto_major avg `-0.14` n `8`; equity avg `0.0512` n `67`; fx avg `-0.0042` n `6`; index avg `0.0694` n `23`; metal avg `-0.3272` n `18`; unknown avg `0.7588` n `376`
- 24h: commodity avg `-0.4597` n `12`; crypto_alt avg `1.6971` n `228`; crypto_major avg `-0.0633` n `8`; equity avg `1.6065` n `67`; fx avg `0.1268` n `6`; index avg `0.7588` n `23`; metal avg `0.5892` n `18`; unknown avg `1.742` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0411`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0401`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0393`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0371`, n `668`, weak_sample_signal
